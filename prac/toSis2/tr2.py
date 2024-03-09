import re

txt = "abcd asdgrw iheurbg piasbg pjvn seorutv apseof hveoif 1294 youwyve f834 vusf oiuwevr aoi shbr uvtwraoi sbgyr vap ouh"

pattern = r"\S*a\S*"
pat2 = r"\S*[0-9]\S*"

x = re.findall(pattern, txt)
y = re.findall(pat2, txt)

print(x)
print(y)