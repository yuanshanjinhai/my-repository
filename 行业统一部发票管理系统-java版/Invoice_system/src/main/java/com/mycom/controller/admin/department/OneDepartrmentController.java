package com.mycom.controller.admin.department;

import com.mycom.service.admin.department.OneDepartrmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class OneDepartrmentController {

    @Autowired
    OneDepartrmentService oneDepatrmentService;

    @GetMapping("one_department")
    public LinkedHashMap  OneDepartment(@RequestParam Integer departmentId){
        return oneDepatrmentService.GetOneDepartment(departmentId);
    }
}
// http://127.0.0.1:5003/one_department?departmentId=12