using Microsoft.EntityFrameworkCore;

namespace TVStore.Models
{
    public class TVContext : DbContext
    {
        public DbSet<TV> TVs { get; set; }
        public DbSet<Order> Orders { get; set; }

        public TVContext(DbContextOptions<TVContext> options)
            : base(options)
        {
            Database.EnsureCreated();
        }
    }
}

