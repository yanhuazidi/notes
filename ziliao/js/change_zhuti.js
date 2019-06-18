//动态加载一个js/css文件
function loadjscssfile(filename, filetype) {
    if (filetype == "js") {
        varfileref = document.createElement('script')
        fileref.setAttribute("type", "text/javascript")
        fileref.setAttribute("src", filename)
    } else if (filetype == "css") {
        var fileref = document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", filename)
    }
    if (typeof fileref != "undefined")
        document.getElementsByTagName("head")[0].appendChild(fileref)
}


//移动已经加载过的js/css
function removejscssfile(filename, filetype) {
    var targetelement = (filetype == "js") ? "script" : (filetype == "css") ? "link" : "none"
    var targetattr = (filetype == "js") ? "src" : (filetype == "css") ? "href" : "none"
    var allsuspects = document.getElementsByTagName(targetelement)
    for (var i = allsuspects.length; i >= 0; i--) {
        if (allsuspects[i] && allsuspects[i].getAttribute(targetattr) != null && allsuspects[i].getAttribute(targetattr).indexOf(filename) != -1)
            allsuspects[i].parentNode.removeChild(allsuspects[i])
    }
}


window.onload = function() {
    var div = document.createElement('div');
    var btn1 = document.createElement('button');
    var btn2 = document.createElement('button');
    var btn3 = document.createElement('button');
    div.style.setProperty('border', '1px solid rgb(253, 186, 0)');
    div.style.setProperty('position', 'fixed');
    div.style.setProperty('top', '10px');
    div.style.setProperty('right', '10px');
    div.style.setProperty('font-size', '18px');
    btn1.style.setProperty('color', '#000');
    btn2.style.setProperty('color', '#000');
    btn3.style.setProperty('color', '#000');
    btn1.innerText = "回到顶部"
    btn2.innerText = "白天模式"
    btn3.innerText = "夜间模式"
    btn1.onclick = function() {
        window.location.href = "#"
    }
    btn2.onclick = function() {
        loadjscssfile('/css/github.dark.css', 'css')
        removejscssfile('/css/night.dark.css', 'css')
    }
    btn3.onclick = function() {
        loadjscssfile('/css/night.dark.css', 'css')
        removejscssfile('/css/github.dark.css', 'css')
    }
    document.body.appendChild(div);
    div.appendChild(btn1)
    div.appendChild(btn2)
    div.appendChild(btn3);
}