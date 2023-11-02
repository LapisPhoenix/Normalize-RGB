![icon](icon_transparent.png)

# Normalize RGB (and RGBA)
The Normalize RGB library simplifies the process of normalizing RGB and RGBA values, ensuring they fall within the standard range of 0 to 1. This functionality is particularly useful for applications like OpenGL and other systems that require normalized color inputs.

# Usage

```python
import normalized_rgb

RED = 150
GREEN = 78
BLUE = 23
ALPHA = 128

print(normalized_rgb.rgb(RED, GREEN, BLUE))
# Output: (0.5882352941176471, 0.3058823529411765, 0.09019607843137255)
print(normalized_rgb.rgba(RED, GREEN, BLUE, ALPHA))
# Output: (0.5882352941176471, 0.3058823529411765, 0.09019607843137255, 0.5019607843137255)
```

# License
This project uses the __[MIT](LICENSE)__