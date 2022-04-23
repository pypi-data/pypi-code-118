import torch.nn as nn
from bert_seq2seq.basic_bert import BasicBert
from bert_seq2seq.layers import GlobalPointer, CRFLayer

class BertSequenceLabling(BasicBert):
    """
    """
    def __init__(self, word2ix, target_size, model_name="roberta", **kwargs):
        super(BertSequenceLabling, self).__init__(word2ix=word2ix, model_name=model_name)
        self.cls.predictions.decoder = None
        self.layer_norm_cond = None
        self.final_dense = nn.Linear(self.config.hidden_size, target_size)

    def compute_loss(self, predictions, labels):
        """
        计算loss
        predictions: (batch_size, 1)
        """
        predictions = predictions.view(-1, self.target_size)
        labels = labels.view(-1)
        loss = nn.CrossEntropyLoss(reduction="mean")
        return loss(predictions, labels)
    
    def forward(self, **data):

        input_ids = data["input_ids"]
        token_type_ids = data["token_type_ids"]
        labels = data.get("labels", None)
        input_tensor = input_ids.to(self.device)
        token_type_id = token_type_ids.to(self.device)
        if labels is not None:
            labels = labels.to(self.device)

        all_layers, pooled_out = self.bert(input_tensor, token_type_ids=token_type_id,
                                    output_all_encoded_layers=True)

        sequence_out = all_layers[-1]
        tokens_hidden_state = self.cls.predictions.transform(sequence_out)
        predictions = self.final_dense(tokens_hidden_state)

        return_data = {"logits": predictions, }

        if labels is not None:
            ## 计算loss
            loss = self.compute_loss(predictions, labels)
            return_data["loss"] = loss

        return return_data

class BertNERGP(BasicBert):
    """
    """
    def __init__(self, word2ix, ent_type_size, inner_dim=64, model_name="roberta", **kwargs):
        super(BertNERGP, self).__init__(word2ix=word2ix, model_name=model_name)
        self.gp = GlobalPointer(self.config.hidden_size, ent_type_size, inner_dim, RoPE=True)
        self.layer_norm_cond = None
        self.cls = None
    def compute_loss(self, logits, labels):
        pass

    def forward(self, **data):
        input_ids = data["input_ids"]
        token_type_ids = data.get("token_type_ids", None)
        padding_mask = (input_ids > 0).float()
        labels = data.get("labels", None)

        all_layers, _ = self.bert(input_ids, token_type_ids=token_type_ids,
                                  output_all_encoded_layers=True)
        sequence_out = all_layers[-1]

        gp_out = self.gp(sequence_out, padding_mask)
        return_data = {"logits": gp_out, }

        if labels is not None:
            return_data["loss"] = self.gp.compute_loss(gp_out, labels)
        return return_data

class BertNERCRF(BasicBert):
    """
    """
    def __init__(self, word2ix, target_size=-1, model_name="roberta", **kwargs):
        super(BertNERCRF, self).__init__(word2ix=word2ix, model_name=model_name)
        self.layer_norm_cond = None
        self.cls = None
        self.final_dense = nn.Linear(self.config.hidden_size, target_size)
        self.crf_layer = CRFLayer(target_size)

    def compute_loss(self, logits, labels, target_mask):
        loss = self.crf_layer(logits, labels, target_mask)

        return loss.mean()

    def forward(self, **data):
        input_ids = data["input_ids"]
        token_type_ids = data.get("token_type_ids", None)
        padding_mask = (input_ids > 0).float()
        labels = data.get("labels", None)

        all_layers, _ = self.bert(input_ids, token_type_ids=token_type_ids,
                                  output_all_encoded_layers=True)
        sequence_out = all_layers[-1]

        predictions = self.final_dense(sequence_out)

        return_data = {"logits": predictions, }

        if labels is not None:
            ## 计算loss
            return_data["loss"] = self.compute_loss(predictions, labels, padding_mask)

        return return_data