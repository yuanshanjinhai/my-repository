package com.mycom.controller.admin.department;

import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.service.admin.department.UpdateDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class UpdateDepartmentController {

    @Autowired
    UpdateDepartmentService updateDepartmentService;

    @PostMapping("/update_department")
    public LinkedHashMap updateDepatment(@RequestBody SystemDepartmentEntity systemDepartmentEntity){
        return updateDepartmentService.updateDepartment(systemDepartmentEntity);
    }
}
// http://127.0.0.1:5003/update_department
// {"id":11,"department_name":"人力资源部","department_explain":"玩你没商量"}