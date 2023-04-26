package com.mycom.controller.admin.company;

import com.mycom.entity.SystemCompanyEntity;
import com.mycom.service.admin.company.UpdateCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.LinkedHashMap;

@Controller
public class UpdateCompanyController {
    @Autowired
    UpdateCompanyService updateCompanyService;

    @PostMapping("/update_company")
    @ResponseBody
    public LinkedHashMap updateCompany(@RequestBody SystemCompanyEntity systemCompanyEntity){
        return updateCompanyService.updateCompany(systemCompanyEntity);
    }
}
//http://127.0.0.1:5003/update_company
//{"id":7,"company_name":"飞奔","company_abbreviation":"你好飞奔","company_explain":"飞奔集团，飞奔帝国"}
