package com.mycom.service.impl.admin.company;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.service.admin.company.OneCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class OneCompanyImpl extends ServiceImpl<SystemCompanyMapper, SystemCompanyEntity> implements OneCompanyService {
    @Autowired
    SystemCompanyMapper systemCompanyMapper;

    @Override
    public LinkedHashMap GetOneCompany(Integer companyId){
        SystemCompanyEntity sce = systemCompanyMapper.selectById(companyId);
        Map lmpd = new HashMap<String,Object>();
        lmpd.put("id",sce.getId());
        lmpd.put("company_name",sce.getCompany_name());
        lmpd.put("company_abbreviation",sce.getCompany_abbreviation());
        lmpd.put("company_explain",sce.getCompany_explain());

        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",lmpd);
        return (LinkedHashMap) lmp;
    }
}
