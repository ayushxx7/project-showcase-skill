#!/bin/bash

# Documentation Build & Serve Script 📚

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Checking for MkDocs...${NC}"

if ! command -v mkdocs &> /dev/null
then
    echo -e "${BLUE}Installing mkdocs-material...${NC}"
    pip install mkdocs-material
fi

echo -e "${GREEN}Documentation is ready!${NC}"
echo -e "${BLUE}Running 'mkdocs serve' to preview...${NC}"
echo -e "Visit: ${GREEN}http://127.0.0.1:8000${NC}"

mkdocs serve
