package com.mycom.service.impl.admin.department;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.mapper.SystemDepartmentListByCompanyMapper;
import com.mycom.model.SystemDepartmentListByCompanyVO;
import com.mycom.service.admin.department.AllDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class AllDepartmentImpl extends ServiceImpl<SystemDepartmentListByCompanyMapper, SystemDepartmentListByCompanyVO> implements AllDepartmentService {
    @Autowired
    SystemDepartmentListByCompanyMapper systemCompanyDepartmentMapper;

    @Override
    public LinkedHashMap GetAllDepartment(Integer companyId){
        List rlist = systemCompanyDepartmentMapper.selectAllDepartmentByCompanyId(companyId);
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap)lmp;
    }
}
