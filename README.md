## What happens if I try to access other stuff in here?
It seems I can't run python or any other "dynamic something-something" in a webpage as it only serves static stuff

**So**, maybe we use javascript?

<div id="helo"></div>
<div id="mebbe"></div>

<script>
  document.getElementById("helo").innerHTML = "Text added by JavaScript code";
  document.getElementById("mebbe"),innerHTML = "'p";
  readTextFile("file://C:\Users\Algor\Documents\Openpose\openpose-master\README.md");
  document.getElementById("mebbe"),innerHTML = "'lp";
  document.getElementById("mebbe"),innerHTML = readTextFile("file://C:\Users\Algor\Documents\Openpose\openpose-master\README.md");
  document.getElementById("mebbe"),innerHTML = "'elp";
  readTextFile("file://A_Close_keypoints.json");
  document.getElementById("mebbe"),innerHTML = "help";
  document.getElementById("mebbe"),innerHTML = readTextFile("file://A_Close_keypoints.json");
  
  function readTextFile(file)
  {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    rawFile.send(null);
  }
</script>


## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/ethanosullivan-wip/Some_DanceDanceDoppelution_Testing/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ethanosullivan-wip/Some_DanceDanceDoppelution_Testing/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
