# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API  # noqa: E501

    The version of the OpenAPI document: v0.1.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from jobset.configuration import Configuration


class JobsetV1alpha2Coordinator(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'job_index': 'int',
        'pod_index': 'int',
        'replicated_job': 'str'
    }

    attribute_map = {
        'job_index': 'jobIndex',
        'pod_index': 'podIndex',
        'replicated_job': 'replicatedJob'
    }

    def __init__(self, job_index=None, pod_index=None, replicated_job='', local_vars_configuration=None):  # noqa: E501
        """JobsetV1alpha2Coordinator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._job_index = None
        self._pod_index = None
        self._replicated_job = None
        self.discriminator = None

        if job_index is not None:
            self.job_index = job_index
        if pod_index is not None:
            self.pod_index = pod_index
        self.replicated_job = replicated_job

    @property
    def job_index(self):
        """Gets the job_index of this JobsetV1alpha2Coordinator.  # noqa: E501

        JobIndex is the index of Job which contains the coordinator pod (i.e., for a ReplicatedJob with N replicas, there are Job indexes 0 to N-1). Defaults to 0 if unset.  # noqa: E501

        :return: The job_index of this JobsetV1alpha2Coordinator.  # noqa: E501
        :rtype: int
        """
        return self._job_index

    @job_index.setter
    def job_index(self, job_index):
        """Sets the job_index of this JobsetV1alpha2Coordinator.

        JobIndex is the index of Job which contains the coordinator pod (i.e., for a ReplicatedJob with N replicas, there are Job indexes 0 to N-1). Defaults to 0 if unset.  # noqa: E501

        :param job_index: The job_index of this JobsetV1alpha2Coordinator.  # noqa: E501
        :type: int
        """

        self._job_index = job_index

    @property
    def pod_index(self):
        """Gets the pod_index of this JobsetV1alpha2Coordinator.  # noqa: E501

        PodIndex is the Job completion index of the coordinator pod. Defaults to 0 if unset.  # noqa: E501

        :return: The pod_index of this JobsetV1alpha2Coordinator.  # noqa: E501
        :rtype: int
        """
        return self._pod_index

    @pod_index.setter
    def pod_index(self, pod_index):
        """Sets the pod_index of this JobsetV1alpha2Coordinator.

        PodIndex is the Job completion index of the coordinator pod. Defaults to 0 if unset.  # noqa: E501

        :param pod_index: The pod_index of this JobsetV1alpha2Coordinator.  # noqa: E501
        :type: int
        """

        self._pod_index = pod_index

    @property
    def replicated_job(self):
        """Gets the replicated_job of this JobsetV1alpha2Coordinator.  # noqa: E501

        ReplicatedJob is the name of the ReplicatedJob which contains the coordinator pod.  # noqa: E501

        :return: The replicated_job of this JobsetV1alpha2Coordinator.  # noqa: E501
        :rtype: str
        """
        return self._replicated_job

    @replicated_job.setter
    def replicated_job(self, replicated_job):
        """Sets the replicated_job of this JobsetV1alpha2Coordinator.

        ReplicatedJob is the name of the ReplicatedJob which contains the coordinator pod.  # noqa: E501

        :param replicated_job: The replicated_job of this JobsetV1alpha2Coordinator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and replicated_job is None:  # noqa: E501
            raise ValueError("Invalid value for `replicated_job`, must not be `None`")  # noqa: E501

        self._replicated_job = replicated_job

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobsetV1alpha2Coordinator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobsetV1alpha2Coordinator):
            return True

        return self.to_dict() != other.to_dict()
