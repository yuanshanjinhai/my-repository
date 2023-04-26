package com.mycom.service.invoice;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.InvoiceInvoiceEntity;

import java.util.LinkedHashMap;

public interface OneInvoiceService extends IService<InvoiceInvoiceEntity> {
    public LinkedHashMap GetOneInvoice(Integer invoiceId);
}
