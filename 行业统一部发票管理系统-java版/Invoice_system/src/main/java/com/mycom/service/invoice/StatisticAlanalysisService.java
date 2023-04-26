package com.mycom.service.invoice;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.InvoiceInvoiceEntity;

import java.util.Date;
import java.util.LinkedHashMap;

public interface StatisticAlanalysisService extends IService<InvoiceInvoiceEntity> {
    public LinkedHashMap statisticAlanalysis(Integer companyId, Integer departmentId, Integer productId, Integer userId, Date startTime, Date endTime);
}
