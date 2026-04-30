import os

with open('index.html', 'r') as f:
    content = f.read()

with open('reviews.html', 'r') as f:
    reviews_html = f.read()

# Replace the marquee container classes
target_container = '<div class="relative flex w-full overflow-hidden [mask-image:_linear-gradient(to_right,transparent_0,_black_100px,_black_calc(100%-100px),transparent_100%)] py-4"'
replacement_container = '<div class="relative flex w-full overflow-hidden [mask-image:_linear-gradient(to_right,transparent_0,_black_100px,_black_calc(100%-100px),transparent_100%)] pt-44 pb-8 -mt-32 z-10"'
content = content.replace(target_container, replacement_container)

# Replace the inner marquee content
start_marker = '<!-- Les logos originaux -->'
end_marker = '</div>\n        </div>\n    </section>\n\n    <!-- Process Section -->'

start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find('            </div>\n        </div>\n    </section>\n\n    <!-- Process Section -->')

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + "\n" + reviews_html + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Markers not found")
