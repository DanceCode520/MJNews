// 登录页面
function goToLogin() {
    console.log("go to loging")
    window.location.href = "login"
}

// 新闻列表页面
function goToNews(ntype) {
    const url="/bknewslist/"+ntype;
    window.location.href = url;
}

// 页面详情
function goToDetail(id) {
    console.log("id==" + id)
    window.location.href = "news/dm?id=" + id;
}

// 获取文件
function getFile(id, index) {
    const ntype = document.getElementById('mjselect');
    const typeindex = ntype.selectedIndex;
    const nindex = ntype.options[typeindex].value;
    if (index == "2") {
        deleteNews(id,nindex);
        return;
    }
    const myfile = document.getElementById("mjfile");
    const file = myfile.files[0];
    let datastr = 'type=' + nindex + "&";
    if (typeof (file) == 'undefined') {
        const imgSrc = document.getElementById('mjimg').src;
        urlArr = imgSrc.split('/')
        datastr += "filename=" + urlArr[urlArr.length - 1] + "&"
        doDB();
        return;
    }
    console.log("file===" + file.name);
    const fileRd = new FileReader();
    fileRd.readAsDataURL(file);
    fileRd.onload = function (ev) {
        // 获取到FileReader读取文件的base64
        oImgBase64 = ev.currentTarget.result;
        datastr += 'filedata=' + oImgBase64 + "&filename=" + uniformStr(file.name) + "&";
        doDB();
    }

    function doDB() {
        if (index == '0') {  //插入
            insert(datastr,nindex);
        } else {  //修改
            change(id,datastr,nindex)
        }
    }
}

// 清空数据内容
function clearAll() {
    document.getElementById("title").value = "";
    document.getElementById("writer").value = "";
    document.getElementById("content8").innerHTML = "";
    document.getElementById("date").value = new Date().Format("yyyy-MM-dd");
}

// 修改新闻信息
function change(id, str,ntype) {
    let sendStr = str;
    const title = document.getElementById("title").value;
    const writer = document.getElementById("writer").value;
    const content = document.getElementById("content8").value;
    const time = document.getElementById("date").value;
    if (title == "" || writer == "" || content == "" || time == "") {
        alert("can not be null")
        return
    }
    let success = ""
    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            success = xmlhttp.responseText;
            console.log("success==" + success);
            goToNews(ntype);
        }
    }
    xmlhttp.open("POST", "/change/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    sendStr += "title=" + title + "&writer=" + writer + "&content=" +
        content + "&time=" + time + "&id=" + id
    console.log(sendStr);
    xmlhttp.send(sendStr);
}

// 插入新闻
function insert(str,ntype) {
    let sendStr = str;
    const title = document.getElementById("title").value;
    const writer = document.getElementById("writer").value;
    const content = document.getElementById("content8").value;
    const time = document.getElementById("date").value;
    let success = ""
    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            success = xmlhttp.responseText;
            console.log("success==" + success);
            goToNews(ntype);
        }
    }
    xmlhttp.open("POST", "/insert/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    sendStr += "title=" + title + "&writer=" + writer + "&content=" +
        content + "&time=" + time
    console.log(sendStr);
    xmlhttp.send(sendStr);
}

// 删除新闻
function deleteNews(id,ntype) {
    console.log('newsId==' + id)
    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            const success = xmlhttp.responseText;
            console.log("success==" + success);
            goToNews(ntype);
        }
    }
    xmlhttp.open("POST", "/delete", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    const sendStr = "id=" + id
    xmlhttp.send(sendStr);
}

// file 改变
function fileChange() {
    var myfile = document.getElementById("mjfile")
    const img = document.getElementById('mjimg')
    var file = myfile.files[0];
    const fileRd = new FileReader();
    fileRd.readAsDataURL(file);
    fileRd.onload = function (ev) {
        // 获取到FileReader读取文件的base64
        oImgBase64 = ev.currentTarget.result;
        console.log(oImgBase64)
        img.src = ev.target.result;
    }
}

// 统一数据格式
function uniformStr(str) {
    var formatStr = str;
    formatStr = formatStr.replace(/&/g, "").formatStr = formatStr.replace(/=/g, "");
    return formatStr;
}

function requestDB(url, method, params) {
    $.ajax({
        //请求方式
        type: method,
        //请求的媒体类型
        dataType: "json",
        // contentType: "application/json;charset=UTF-8",
        //请求地址
        url: url,
        //数据，json字符串
        data: params,
        //请求成功
        success: function (result) {
            console.log(result);
        },
        //请求失败，包含具体的错误信息
        error: function (e) {
            console.log(e.status);
            console.log(e.responseText);
        }
    });
}

// 点击新闻类别
// window.onload = function () {
//     aTags = document.getElementsByTagName("a")
//     console.log('lent==' + aTags.length)
//     for (let i=0;i<aTags.length;i++){
//         const aT=aTags[i]
//         aT.onmousedown=function () {
//             console.log('click==='+i)
//             removeCover();
//             aT.classList.add('cover')
//         }
//     }
//
//     function removeCover() {
//         for (let i=0;i<aTags.length;i++){
//             aTags[i].classList.remove('cover')
//         }
//     }
// }