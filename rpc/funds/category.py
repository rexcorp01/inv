from rpc import models

from rpc.services import funds_pb2 as pb


@models.async_database
async def fund_category_new(request: pb.FundCategoryRequest, context):
    """新的基金分类"""
    funds = request.fund
    c = models.Classify
    sql = models.sa.select([c.c.windcode_id, c.c.classify]).where(c.c.windcode_id.in_(funds)).distinct()
    funds = await models.database.fetch_all(sql)
    data = [pb.FundCategory(secucode=x[0], category=x[1]) for x in funds]
    return pb.FundCategoryResponse(status_code=0, data=data)
