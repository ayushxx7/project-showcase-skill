import unittest
import os
import re

def mock_inject_showcase(content, showcase_block):
    """
    Mocked logic for surgical injection of the showcase gallery.
    This simulates the logic the agent should follow.
    """
    marker = "## 🎬 Showcase Gallery"
    if marker in content:
        # Replace existing gallery
        return re.sub(rf"{marker}.*?(?=##|\Z)", showcase_block + "\n", content, flags=re.DOTALL)
    else:
        # Append before Tech Stack or at the end
        if "## 🛠️ Tech Stack" in content:
            return content.replace("## 🛠️ Tech Stack", f"{showcase_block}\n\n## 🛠️ Tech Stack")
        return content + f"\n\n{showcase_block}"

class TestReadmeInjection(unittest.TestCase):
    def test_inject_new_showcase(self):
        original = "# My Project\nExisting dev notes here."
        showcase = "## 🎬 Showcase Gallery\n![Demo](showcase/demo.gif)"
        result = mock_inject_showcase(original, showcase)
        
        self.assertIn("Existing dev notes here.", result)
        self.assertIn("## 🎬 Showcase Gallery", result)

    def test_replace_existing_showcase(self):
        original = "# My Project\n## 🎬 Showcase Gallery\nOld stuff\n## 🛠️ Tech Stack"
        showcase = "## 🎬 Showcase Gallery\nNew high-res demo!"
        result = mock_inject_showcase(original, showcase)
        
        self.assertIn("# My Project", result)
        self.assertIn("New high-res demo!", result)
        self.assertNotIn("Old stuff", result)
        self.assertIn("## 🛠️ Tech Stack", result)

    def test_preservation_of_manual_docs(self):
        original = "# My Project\n## How it Works\nImportant manual info.\n## 🛠️ Tech Stack"
        showcase = "## 🎬 Showcase Gallery\n![Demo](showcase/demo.gif)"
        result = mock_inject_showcase(original, showcase)
        
        self.assertIn("Important manual info.", result)
        self.assertIn("## 🎬 Showcase Gallery", result)
        self.assertTrue(result.find("## How it Works") < result.find("## 🎬 Showcase Gallery"))

if __name__ == "__main__":
    unittest.main()
