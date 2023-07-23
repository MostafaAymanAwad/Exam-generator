#region Using ...
using Framework.Common.Enums;
using System;
using System.Collections.Generic;
using System.Linq.Expressions;
using System.Text;
#endregion

/*


 */
namespace Framework.Core.Common
{
	/// <summary>
	/// 
	/// </summary>
	/// <typeparam name="TEntity"></typeparam>
	/// <typeparam name="TKey"></typeparam>
	public class RepositoryRequestConditionFilter<TEntity, TKey> : RepositoryRequest
	{
		#region Data Members

		#endregion

		#region Constructors
		/// <summary>
		/// Initializes a new instance from type 
		/// RepositoryRequestConditionFilter.
		/// </summary>
		public RepositoryRequestConditionFilter(RepositoryRequest repositoryRequest)
			: base(repositoryRequest)
		{

		}
		/// <summary>
		/// Initializes a new instance from type 
		/// RepositoryRequestConditionFilter.
		/// </summary>
		public RepositoryRequestConditionFilter()
		{

		}
		#endregion

		#region Properties
		public Expression<Func<TEntity, bool>> Query { get; set; }
		#endregion
	}
}