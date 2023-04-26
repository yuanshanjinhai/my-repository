package com.mycom.controller.invoice;

import com.mycom.service.invoice.StatisticAlanalysisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;
import java.util.LinkedHashMap;

@RestController
public class StatisticAlanalysisController {
    @Autowired
    StatisticAlanalysisService statisticAlanalysisService;

    @GetMapping("/statistic_alanalysis")
    public LinkedHashMap StatisticAlanalysis(@RequestParam(value = "companyId",required=false) Integer companyId,
                                             @RequestParam(value = "departmentId",required=false) Integer departmentId,
                                             @RequestParam(value = "productId",required=false) Integer productId,
                                             @RequestParam(value = "userId",required=false) Integer userId,
                                             @RequestParam(value = "startTime",required=false) Date startTime,
                                             @RequestParam(value = "endTime",required=false) Date endTime){
        return statisticAlanalysisService.statisticAlanalysis(companyId,departmentId,productId,userId,startTime,endTime);
    }
}
