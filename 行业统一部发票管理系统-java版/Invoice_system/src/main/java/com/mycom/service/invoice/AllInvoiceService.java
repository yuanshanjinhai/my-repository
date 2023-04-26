package com.mycom.service.invoice;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.InvoiceInvoiceEntity;

import java.util.LinkedHashMap;

public interface AllInvoiceService extends IService<InvoiceInvoiceEntity> {
    public LinkedHashMap GetAllInvoice(Integer companyId,Integer departmentId,Integer productId,Integer userId);
}
