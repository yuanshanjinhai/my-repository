package com.mycom.service.invoice;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.InvoiceInvoiceEntity;

import java.util.LinkedHashMap;

public interface InsertInvoiceService extends IService<InvoiceInvoiceEntity> {
    public LinkedHashMap InsertInvoice(InvoiceInvoiceEntity invoiceInvoiceEntity);
}
