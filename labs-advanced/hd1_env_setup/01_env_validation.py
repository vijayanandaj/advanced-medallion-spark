# Databricks notebook source
# MAGIC %md
# MAGIC # H1 — Environment Setup & Validation
from utils.widgets import get_widgets
print("Using:", *get_widgets())
print("Checklist: DBR 15.x + Photon, secrets configured, UC schema exists")
