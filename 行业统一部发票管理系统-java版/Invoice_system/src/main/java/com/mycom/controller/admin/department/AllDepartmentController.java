package com.mycom.controller.admin.department;

import com.mycom.service.admin.department.AllDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.LinkedHashMap;

@Controller
public class AllDepartmentController {
    @Autowired
    AllDepartmentService allDepartmentService;

    @GetMapping ("/all_department")
    @ResponseBody
    public LinkedHashMap GetAllDepartment(@RequestParam Integer companyId){
        return allDepartmentService.GetAllDepartment(companyId);
    }
}
// http://127.0.0.1:5003/all_department?companyId=3