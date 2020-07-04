# anti_harassment_tools

DISCLAIMER: This script and shortcut may only be used on your own property! Do not use this code if you do not own the domains/phone numbers or have permission from the owner of the domains/phone numbers.  

## Intructions:
1. You need to download the selenium Firefox driver and put it in the root directory of this project.
2. Run `export PATH=$PATH:` in root of project
3. Run `pip3 install -r requirements.txt` (Ubuntu) or `pip install -r requirements.txt` (MacOS)
4. Go to your website and into the url that has the form. Copy that url into the `URL` constant.
5. In your form right click one of the inputs and select "Inspect element". Right click the HTML for the input and select "Copy -> Copy xPath". Note: Some browsers have the option "Copy full xpath" it did not work for me.
6. Paste the xpath into a `find_element_by_xpath` function and save it in a nicely named attribute.
7. In the `apply()` method and fill in the data of your elements with garbage.
8. Run `python3 post_mania.py` (Ubuntu) or `python post_mania.py` (MacOS)
9. Sit back and relax :)

# Shortcut
You can find the shortcut here: https://www.icloud.com/shortcuts/3a4e4d8e97e745e7a6bfbf11638734a3
Note: The shortcut may not run more than 50 times. Still it's pretty good to make 50 calls with just one click.