// ==UserScript==
// @name         seuVisitor
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  一键实现车牌预约，需手动填写信息
// @author       Romanticoseu
// @match        https://infoplus.seu.edu.cn/infoplus/form/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=seu.edu.cn
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    let myCarId = '';
    let myDomitory = '';
    let myDepartmentId = '';
    let myDepartmentName = '';
    let myDaoyuanId = '';
    let myDaoyuanName = '';
    let myDaoyuanPhone = '';
    let myReason = '';
    function handleCheckbox(checkBoxs) {
        for (let checkBox of checkBoxs) {
            checkBox.click();
        }
    }
    function CompleteForm() {
        var checkBoxs = [];
        var parentIs = document.getElementById("V1_CTRL390");
        var commiment = document.getElementById("V1_CTRL267");
        var campusLonghu = document.getElementById("V1_CTRL274");
        var driverIs = document.getElementById("V1_CTRL215");
        checkBoxs.push(parentIs, commiment, campusLonghu, driverIs);
        handleCheckbox(checkBoxs);

        var carId = document.getElementById("V1_CTRL217");
        carId.value = myCarId;
        var domitoryArea = document.getElementById("V1_CTRL376");
        domitoryArea.value = myDomitory;

        var department = document.getElementById("V1_CTRL377");
        var departmentOption = document.createElement("option");
        departmentOption.value = myDepartmentId;
        departmentOption.text = myDepartmentName;
        department.appendChild(departmentOption);
        department.value = myDepartmentId;

        var daoyuan = document.getElementById("V1_CTRL378");
        var daoyuanOption = document.createElement("option");
        daoyuanOption.value = myDaoyuanId;
        daoyuanOption.text = myDaoyuanName;
        daoyuan.appendChild(daoyuanOption);
        daoyuan.value = myDaoyuanId;

        var daoyuanPhone = document.getElementById("V1_CTRL379");
        daoyuanPhone.value = myDaoyuanPhone;
        var reason = document.getElementById("V1_CTRL380");
        reason.value = myReason;
    }

    window.onload = function () {
        console.log("网页加载完毕！");
        setTimeout(function () {
            CompleteForm();
        }, 1000);
    };
})();
