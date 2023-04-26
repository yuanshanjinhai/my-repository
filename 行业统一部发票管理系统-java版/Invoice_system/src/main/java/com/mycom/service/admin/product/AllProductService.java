package com.mycom.service.admin.product;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemProductEntity;

import java.util.LinkedHashMap;

public interface AllProductService extends IService<SystemProductEntity> {
    public LinkedHashMap GetAllProduct(String productName);
}
