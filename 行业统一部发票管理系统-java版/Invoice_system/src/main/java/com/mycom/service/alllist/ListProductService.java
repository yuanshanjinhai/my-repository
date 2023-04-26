package com.mycom.service.alllist;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemProductEntity;

import java.util.LinkedHashMap;

public interface ListProductService extends IService<SystemProductEntity> {
    public LinkedHashMap GetProductList();
}
