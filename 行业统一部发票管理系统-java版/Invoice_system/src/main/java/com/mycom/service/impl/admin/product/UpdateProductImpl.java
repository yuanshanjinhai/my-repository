package com.mycom.service.impl.admin.product;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemProductEntity;
import com.mycom.mapper.SystemProductMapper;
import com.mycom.service.admin.product.UpdateProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class UpdateProductImpl extends ServiceImpl<SystemProductMapper, SystemProductEntity> implements UpdateProductService {
    @Autowired
    SystemProductMapper systemProductMapper;

    @Override
    public LinkedHashMap UpdateProdect(SystemProductEntity systemProductEntity){
        String productName = systemProductEntity.getProduct_name();
        String productAbbreviation = systemProductEntity.getProduct_abbreviation();
        String productExplain = systemProductEntity.getProduct_explain();
        Map lmp = new LinkedHashMap();

        String errorStr = "";
        if(productName == null){
            errorStr += "项目名称不能为空；";
        }
        if(productName.length() > 50){
            errorStr += "项目名称不能超过50个字；";
        }
        if(productAbbreviation.length() > 30){
            errorStr += "项目简称不能超过30个字；";
        }
        if(productExplain.length() > 1000){
            errorStr += "项目说明不能超过1000个字；";
        }

        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            int r = systemProductMapper.updateById(systemProductEntity);
            if(r == 0){
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","插入失败；");
            }
            else {
                lmp.put("code",1);
                lmp.put("info","success");
            }
        }
        return (LinkedHashMap) lmp;
    }
}
