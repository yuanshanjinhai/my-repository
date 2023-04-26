package com.mycom.controller.admin.department;

import com.mycom.model.SystemDepartmentCompanyVO;
import com.mycom.service.admin.department.InsertDepartmenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class InsertDepartmentController {

    @Autowired
    private InsertDepartmenService insertDepartmenService;

    @PostMapping("/insert_department")
    public LinkedHashMap insertDepartment(@RequestBody SystemDepartmentCompanyVO systemDepartmentCompanyVO) {
        return insertDepartmenService.insertDepartment(systemDepartmentCompanyVO);
    }
}
// http://127.0.0.1:5003/insert_department
// {"departmentName":"劳保部2","departmentExplain":"负责劳保用品","companyId":1}
