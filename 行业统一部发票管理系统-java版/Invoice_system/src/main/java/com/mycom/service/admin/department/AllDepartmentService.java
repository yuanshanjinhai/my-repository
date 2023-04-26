package com.mycom.service.admin.department;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.model.SystemDepartmentListByCompanyVO;

import java.util.LinkedHashMap;

public interface AllDepartmentService extends IService<SystemDepartmentListByCompanyVO> {
    public LinkedHashMap GetAllDepartment(Integer companyId);
}
