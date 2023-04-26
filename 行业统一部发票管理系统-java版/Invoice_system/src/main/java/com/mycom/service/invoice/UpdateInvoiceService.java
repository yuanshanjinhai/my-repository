package com.mycom.service.invoice;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.controller.invoice.UpdateInvoiceController;
import com.mycom.entity.InvoiceInvoiceEntity;

import java.util.LinkedHashMap;

public interface UpdateInvoiceService extends IService<InvoiceInvoiceEntity> {
    public LinkedHashMap UpdateInvoice(InvoiceInvoiceEntity invoiceInvoiceEntity);
}
