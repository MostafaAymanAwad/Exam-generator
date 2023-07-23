﻿using System;
using System.Collections.Generic;
using System.Text;

namespace EGService.Core.Models.ViewModels
{
    public class ChangePasswordViewModel : Base.BaseViewModel
    {
        public long UserId { get; set; }
        public string OldPassword { get; set; }
        public string NewPassword { get; set; }
        public string ConfirmPassword { get; set; }

    }
}
