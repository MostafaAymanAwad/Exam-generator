#region Using ...
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
#endregion

/*


 */
namespace Framework.Core.IRepositories
{
	/// <summary>
	/// 
	/// </summary>
	public interface IUnitOfWorkAsync
	{
		#region Methods
		/// <summary>
		/// 
		/// </summary>
		/// <returns></returns>
		Task<int> CommitAsync();
		#endregion
	}
}