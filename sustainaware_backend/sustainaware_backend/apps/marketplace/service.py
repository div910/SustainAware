import openai
import json
import http
import numpy as np
from django.conf import settings
from sustainaware_backend.apps.marketplace.dao import Dao
from django.shortcuts import HttpResponse

openai.api_key = settings.OPENAI_API_KEY

class Recomender:

    def __init__(self):
        self.embedding_mapping = {}

    def recomend_search_results(self, req_body={}):
        response = {'success': True, 'data': [], 'err_list': []}
        query = req_body.get("filters", {}).get("text", None)
        db_resp = Dao().get_all_products()
        if db_resp is None:
            return response
        if query == None or query == '':
            for row in db_resp:
                res = {"image": row.get("image_name", 'default'), "data": row.get("product_description_frontend")}
                # res.update({"payment_type": row.get("payment_type") if row.get("payment_type") else ''})
                response.get('data', []).append(res)
            return response
        response_lis = self.get_similarity_score(query, db_resp)
        for row in response_lis:
            res = {"image": row.get("image_name", 'default'), "data": row.get("product_description_frontend")}
            response.get('data', []).append(res)

        return response

    @staticmethod
    def similary_between_two_vectors(a, b):
        A = np.array(a)
        B = np.array(b)
        return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

    @staticmethod
    def get_embedding_for_similarity(query, model='text-embedding-ada-002'):
        try:
            result = openai.Embedding.create(
                model=model,
                input=query)
            return result["data"][0]["embedding"]
        except Exception as exp:
            print(f"Error in getting embedding for similarity now retrying, err: {exp}")
            try:
                result = openai.Embedding.create(
                    model=model,
                    input=query)
                return result["data"][0]["embedding"]
            except Exception as exp:
                print(f"Error in getting embedding for similarity, err: {exp}")
                return [0] * 1536

    @staticmethod
    def parse_offer_list(offer_str):
        fields = offer_str.split(',')
        category = None
        offer_id = None
        for i, field in enumerate(fields):
            fld = field.strip()
            if i == 0:
                category = fld
            elif i == 1:
                offer_id = fld
        return category, offer_id

    def get_similarity_score(self, query, offers_lis):
        try:
            query_embedding = self.get_embedding_for_similarity(query)
            scores_lis = []
            for i, offer in enumerate(offers_lis):
                if self.embedding_mapping.get(i, None):
                    offer_emb = self.embedding_mapping.get(i)
                else:
                    offer_emb = self.get_embedding_for_similarity(offer)
                    self.embedding_mapping[i] = offer_emb
                score = self.similary_between_two_vectors(query_embedding, offer_emb)
                scores_lis.append((i, score))
            scores_lis = sorted(scores_lis, key=lambda x: x[1], reverse=True)
            result = []
            for i in scores_lis[:10]:
                result.append(offers_lis[i[0]])
            return result
        except Exception as exp:
            print(f"Error in getting similarity score, err: {exp}")
            return []