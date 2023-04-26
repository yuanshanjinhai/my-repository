package com.mycom.service.admin.company;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemCompanyEntity;

import java.util.LinkedHashMap;

public interface OneCompanyService extends IService<SystemCompanyEntity> {
    public LinkedHashMap GetOneCompany(Integer companyId);
}
