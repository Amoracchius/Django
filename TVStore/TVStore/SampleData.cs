using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using TVStore.Models;

namespace TVStore
{
    public class SampleData
    {
        public static void Initialize(TVContext context)
        {
            if (!context.TVs.Any())
            {
                context.TVs.AddRange(
                    new TV
                    {
                        Name = "Samsung UE55RU7172 ",
                        Company = "Samsung",
                        Price = 1500
                    },
                    new TV
                    {
                        Name = "Sony KD-55XG9505 ",
                        Company = "Sony",
                        Price = 1250
                    },
                    new TV
                    {
                        Name = "Vinga S50UHD20B",
                        Company = "Vinga",
                        Price = 1400
                    }
                );
                context.SaveChanges();
            }
        }
    }
}
