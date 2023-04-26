package com.mycom.controller.admin.company;

import com.mycom.entity.SystemCompanyEntity;
import com.mycom.service.admin.company.InsertCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.LinkedHashMap;

@Controller
public class InsertCompanyController {
    @Autowired
    InsertCompanyService insertCompanyService;

    @PostMapping("/insert_company")
    @ResponseBody
    public LinkedHashMap InsertCompany(@RequestBody SystemCompanyEntity systemCompanyEntity){
        return insertCompanyService.InsertCompany(systemCompanyEntity);
    }
}
//http://127.0.0.1:5003/insert_company
//{"company_name":"飞奔","company_abbreviation":"dff放寒假的首付款交h3tyriuhgireu"}