package com.mycom.service.alllist;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemInvoiceTypeEntity;
import java.util.LinkedHashMap;

public interface ListInvoiceTypeService extends IService<SystemInvoiceTypeEntity> {
    public LinkedHashMap GetInvoiceTypeList();
}
