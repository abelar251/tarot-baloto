import re

def fix_days():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the while loop and replace it
    target = 'while (d.getDay() !== 3 && d.getDay() !== 6)'
    replacement = 'while (d.getDay() !== 1 && d.getDay() !== 3 && d.getDay() !== 6)'
    
    if target in content:
        content = content.replace(target, replacement)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Draw days logic updated successfully.")
    else:
        print("Target string not found in index.html.")

if __name__ == '__main__':
    fix_days()
