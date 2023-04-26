package com.mycom.service.alllist;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.model.SystemDepartmentListByCompanyVO;

import java.util.LinkedHashMap;

public interface ListDepartmentService extends IService<SystemDepartmentListByCompanyVO> {
    public LinkedHashMap GeDepartmentList(Integer departId);
}
