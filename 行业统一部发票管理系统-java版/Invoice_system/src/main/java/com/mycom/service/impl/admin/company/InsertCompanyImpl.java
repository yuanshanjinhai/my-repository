package com.mycom.service.impl.admin.company;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.service.admin.company.InsertCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class InsertCompanyImpl extends ServiceImpl<SystemCompanyMapper,SystemCompanyEntity> implements InsertCompanyService {
    @Autowired
    SystemCompanyMapper systemCompanyMapper;

    @Override
    public LinkedHashMap InsertCompany(SystemCompanyEntity systemCompanyEntity){
        String company_name = systemCompanyEntity.getCompany_name();
        String company_abbreviation = systemCompanyEntity.getCompany_abbreviation();
        String company_explain = systemCompanyEntity.getCompany_explain();
        System.out.println("company_abbreviation=" +company_abbreviation);

        Map lmp = new LinkedHashMap();

        String errorStr = "";
        if(company_name == null){
            errorStr += "公司名称不能为空；";
        }
        if(company_name.length() > 50){
            errorStr += "公司名称不能超过50个字；";
        }

        QueryWrapper<SystemCompanyEntity> qw = new QueryWrapper<>();
        List<SystemCompanyEntity> companyNamelist0 = systemCompanyMapper.selectList(qw);
        List companyNamelist = new ArrayList();
        for(int i=0;i<companyNamelist0.size();i++){
            companyNamelist.add(companyNamelist0.get(i).getCompany_name());
        }
        if(companyNamelist.contains(company_name) == true){
            errorStr += "公司名称已存在；";
        }

        if(company_abbreviation != null){
            if(company_abbreviation.length() >30){
                errorStr += "公司简称不能超过30个字；";
            }
        }
        if(company_explain != null){
            if(company_explain.length() > 1000){
                errorStr += "公司说明不能超过1000个字；";
            }
        }

        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            systemCompanyEntity.setCreat_time(new Date());
            Integer r = systemCompanyMapper.insert(systemCompanyEntity);
            if(r == 1){
                lmp.put("code",1);
                lmp.put("info","success");
            }
            else {
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","插入失败；");
            }
        }
        return (LinkedHashMap) lmp;
    }
}
