package com.mycom.service.admin.product;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemProductEntity;

import java.util.LinkedHashMap;

public interface InsertProductService extends IService<SystemProductEntity> {
    public LinkedHashMap InsertProduct(SystemProductEntity systemProductEntity);
}
