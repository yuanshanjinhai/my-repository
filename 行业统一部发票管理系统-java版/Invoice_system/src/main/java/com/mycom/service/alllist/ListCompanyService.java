package com.mycom.service.alllist;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemCompanyEntity;

import java.util.LinkedHashMap;

public interface ListCompanyService extends IService<SystemCompanyEntity> {
    public LinkedHashMap GetCompanyList();
}
