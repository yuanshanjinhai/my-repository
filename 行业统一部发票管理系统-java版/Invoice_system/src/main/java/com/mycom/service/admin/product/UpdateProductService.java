package com.mycom.service.admin.product;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemProductEntity;

import java.util.LinkedHashMap;

public interface UpdateProductService extends IService<SystemProductEntity> {
    public LinkedHashMap UpdateProdect(SystemProductEntity systemProductEntity);
}
