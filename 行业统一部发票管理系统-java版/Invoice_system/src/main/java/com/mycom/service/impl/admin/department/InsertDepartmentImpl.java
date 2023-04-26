package com.mycom.service.impl.admin.department;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyDepartmentEntity;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.mapper.SystemCompanyDepartmentMapper;
import com.mycom.mapper.SystemDepartmentCompanyMapper;
import com.mycom.mapper.SystemDepartmentMapper;
import com.mycom.model.SystemDepartmentCompanyVO;
import com.mycom.service.admin.department.InsertDepartmenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class InsertDepartmentImpl extends ServiceImpl<SystemDepartmentCompanyMapper, SystemDepartmentCompanyVO> implements InsertDepartmenService {
    @Autowired
    SystemDepartmentCompanyMapper systemDepartmentCompanyMapper;
    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;
    @Autowired
    SystemCompanyDepartmentMapper systemCompanyDepartmentMapper;

    @Override
    public LinkedHashMap insertDepartment(SystemDepartmentCompanyVO systemDepartmentCompanyVO){
        String departmentName = systemDepartmentCompanyVO.getDepartmentName();
        String departmentExplain = systemDepartmentCompanyVO.getDepartmentExplain();
        Integer companyId = systemDepartmentCompanyVO.getCompanyId();
        Map lmp = new LinkedHashMap();

        String errorStr = "";
        if(departmentName == null){
            errorStr += "部门名称不能为空；";
        }
        if(departmentName.length() > 30){
            errorStr += "部门名称不能超过50个字；";
        }
        if(departmentExplain.length() > 1000){
            errorStr += "部门说明不能超过1000个字；";
        }
        if(companyId == null){
            errorStr += "未选择公司；";
        }

        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            SystemDepartmentEntity systemDepartmentEntity = new SystemDepartmentEntity();
            systemDepartmentEntity.setDepartment_name(departmentName);
            systemDepartmentEntity.setDepartment_explain(departmentExplain);
            int rDepartment = systemDepartmentMapper.insert(systemDepartmentEntity);

            int newestDepartId = systemDepartmentMapper.selectDepartmentNewest();
            System.out.println("newestDepartId=" +newestDepartId +newestDepartId +newestDepartId);
            System.out.println("companyId=" +companyId);
            SystemCompanyDepartmentEntity systemCompanyDepartmentEntity = new SystemCompanyDepartmentEntity();
            systemCompanyDepartmentEntity.setCompany_id(companyId);
            systemCompanyDepartmentEntity.setDepartment_id(newestDepartId);
            int rCompanyDepartment = systemCompanyDepartmentMapper.insert(systemCompanyDepartmentEntity);

            if (rDepartment == 1 || rCompanyDepartment == 1){
                lmp.put("code",1);
                lmp.put("info","success");
            }
            else {
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","插入失败；");
            }
        }
        return (LinkedHashMap)lmp;
    }
}
