import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the disabled attributes and styles from btn-play-now
new_content = re.sub(
    r'<button id="btn-play-now"([^>]+)disabled([^>]+)opacity:\s*0\.3;([^>]+)pointer-events:\s*none;([^>]*)>',
    r'<button id="btn-play-now"\1\2opacity: 1;\3pointer-events: auto;\4>',
    content
)

if content != new_content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced btn-play-now")
else:
    print("Could not find the disabled button pattern to replace")
