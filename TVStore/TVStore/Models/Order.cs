using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace TVStore.Models
{
    public class Order
    {
        public int OrderId { get; set; }
        public string User { get; set; } // имя фамилия покупателя
        public string Address { get; set; } // адрес покупателя
        public string ContactPhone { get; set; } // контактный телефон покупателя

        public int TVId { get; set; } // ссылка на связанную модель TV
        public TV TV { get; set; }
    }
}
