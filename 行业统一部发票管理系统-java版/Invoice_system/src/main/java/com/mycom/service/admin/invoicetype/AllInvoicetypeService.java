package com.mycom.service.admin.invoicetype;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemInvoiceTypeEntity;

import java.util.LinkedHashMap;

public interface AllInvoicetypeService extends IService<SystemInvoiceTypeEntity> {
    public LinkedHashMap GetAllInvoicetype(SystemInvoiceTypeEntity systemInvoiceTypeEntity);
}
