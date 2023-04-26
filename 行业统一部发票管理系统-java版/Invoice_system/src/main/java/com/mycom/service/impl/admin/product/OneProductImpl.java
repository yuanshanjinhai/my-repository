package com.mycom.service.impl.admin.product;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemProductEntity;
import com.mycom.mapper.SystemProductMapper;
import com.mycom.service.admin.product.OneProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class OneProductImpl extends ServiceImpl<SystemProductMapper, SystemProductEntity> implements OneProductService {
    @Autowired
    SystemProductMapper systemProductMapper;

    @Override
    public LinkedHashMap GetOneProduct(Integer producId){
        SystemProductEntity systemProductEntityResult = systemProductMapper.selectById(producId);
        Map lmp0 = new LinkedHashMap();
        lmp0.put("id",systemProductEntityResult.getId());
        lmp0.put("product_name",systemProductEntityResult.getProduct_name());
        lmp0.put("product_abbreviation",systemProductEntityResult.getProduct_abbreviation());
        lmp0.put("product_explain",systemProductEntityResult.getProduct_explain());

        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",lmp0);
        return (LinkedHashMap) lmp;
    }
}
