package com.mycom.controller.alllist;

import com.mycom.model.SystemDepartmentListByCompanyVO;
import com.mycom.service.alllist.ListDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ListDepartmentController {
    @Autowired
    ListDepartmentService listDepartmentService;

    @GetMapping("/get_department_list")
    @ResponseBody
    public Object GeDepartmentList(SystemDepartmentListByCompanyVO systemCompanyDepartmentModel){
        Integer companyId = systemCompanyDepartmentModel.getCompanyId();
        return listDepartmentService.GeDepartmentList(companyId);
    }
}
//http://127.0.0.1:5003/get_department_list?companyId=1