import os
import shutil
import glob

def bundle_for_linkedin(project_root, output_dir="linkedin_launch"):
    """
    Surgically select and rename the best showcase assets for LinkedIn.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    showcase_dir = os.path.join(project_root, "showcase")
    assets_dir = os.path.join(project_root, "assets")
    
    # Priority patterns
    patterns = [
        ("landing", "01_Landing_Page.png"),
        ("dashboard", "02_Dashboard_View.png"),
        ("architecture", "03_System_Architecture.png"),
        ("demo", "04_CLI_Demo.gif"),
        ("health", "05_Repo_Health.png")
    ]
    
    found_assets = []
    
    # Search in showcase and assets
    search_paths = [showcase_dir, assets_dir, project_root]
    
    for search_dir in search_paths:
        if not os.path.exists(search_dir):
            continue
            
        for key, target_name in patterns:
            # Match case-insensitive
            matches = glob.glob(os.path.join(search_dir, f"*{key}*.[pP][nN][gG]"))
            matches += glob.glob(os.path.join(search_dir, f"*{key}*.[gG][iI][fF]"))
            
            for match in matches:
                dest_path = os.path.join(output_dir, target_name)
                if not os.path.exists(dest_path):
                    shutil.copy2(match, dest_path)
                    found_assets.append(dest_path)
                    print(f"Bundled: {match} -> {dest_path}")
    
    if not found_assets:
        print("No specific showcase assets found. Creating placeholder instructions.")
        with open(os.path.join(output_dir, "INSTRUCTIONS.txt"), "w") as f:
            f.write("No assets found automatically. Please run 'project-showcase' to generate screenshots first.")
    
    return found_assets

if __name__ == "__main__":
    bundle_for_linkedin(".")
