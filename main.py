import htmlpywrite
# take a while to import

# when you open up the web view you will see something like this

# Get dictnary listing
# .something
# stuff
# stuff
# /htmlpywrite/ ---> this is what you need to click to display the web output
# more stuff
# stuff
# stuff
# stuff
# stuff

# to start the index file !!! must be inculded !!!
start = htmlpywrite.start("this is a test")
start.add_body("red", True, "black", 5, "double")
# pls add style classess and not permaters
# it would make my life easyer if i did not have to add more peramters
# built in permateres comming soon

styleClass = htmlpywrite.style(2)  # indention level

styleClass.creat_new_class("complex_button")
styleClass.property("background-color", "DodgerBlue")
styleClass.property("-webkit- border-radius", "5px")
styleClass.property("border-radius", "5px")
styleClass.property("color", "black")
styleClass.property("padding", "2px 5px")
styleClass.property("text-aling", "center")
styleClass.property("display", "inline-block")
styleClass.property("box-shadow", "0 0 10px DodgerBlue;")
styleClass.property("postion", "absolute")
styleClass.property("width", "120px")
styleClass.property("hight", "60px")
styleClass.closeClass()

styleClass.creat_new_class("pythonText")
styleClass.property("background-color", "DodgerBlue")
styleClass.property("color", "red")
styleClass.closeClass()

styleClass.closeStyle()

# add your element like text and buttons
elements = htmlpywrite.elements()
headers = elements.header()
headers.header1("this is a header", "center", "black", True, "black", 5)
headers.header2("this is a secondary header", "center", "green")
elements.maketext("this is a new text", "center", "black", False, True, 23,
                  "blue", 20)
headers.header2("scroll down more below", "center", "yellow")
elements.button("this is a button",
                "blue",
                "black",
                border=True,
                borderRadis=5,
                glowBox=True,
                glowBoxColor="yellow",
                glowBoxSizeInPX=5)
elements.img("html_logo.png")
elements.maketext("this is a image above", "left", "black", False)
headers.header2("made form 100% python", "right", "black", False)
elements.italic("this is a italic text", "center", "black", font_size=23)
elements.boldText("this is a bold text", "right", "black", font_size=20)
elements.maketext("bold does not creat new line", "left", "black", False)
elements.maketext("💀replit is dying💀!", "center", "black", False, font_size=26)
elements.button("button made with css class",
                _class_="complex_button",
                id="buttonId")
elements.maketext("This is a animation", _class_="changetext")
elements.UnderlineText("This is made with python too. :)", _class_="changetext")

# add the replit badge if you like

start.add_annoyedwithreplit_badge()

# add animation to a text with css

stylecss = htmlpywrite.stylecss()

stylecss.creat_new_class(name="changetext")
stylecss.fontsizeStyle(53)
animation = stylecss.animation(name="change_text")
animation.addkeyframe("0%", "color: green; margin-left: 0px;")
animation.addkeyframe("100%", "color: blue; margin-left: 925px;")
animation.closekeyframeClass()

# pyscript: server and excute it when needed in your web page
# no support for flask
# this is a new and powerfull tool: errors may occur
# you can have multible pyscripts in one web page
pyscript = htmlpywrite.pyscript("your Link")
pyscript.pyOpen()

# close the index file and run it !!! must be inculded !!!
htmlpywrite.closeHtml()
htmlpywrite.run(8080)
