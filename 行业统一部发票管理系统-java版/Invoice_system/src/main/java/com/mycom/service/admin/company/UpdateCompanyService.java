package com.mycom.service.admin.company;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemCompanyEntity;

import java.util.LinkedHashMap;

public interface UpdateCompanyService extends IService<SystemCompanyEntity> {
    public LinkedHashMap updateCompany(SystemCompanyEntity systemCompanyEntity);
}
